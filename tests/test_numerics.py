"""Physical/analytic checks, rather than tests that merely mirror code."""
import unittest
import numpy as np
from scripts.numerics import (lj_pair,lj_forces,fcc,velocity_verlet,rdf,msd,
    diffusion_slope,statistical_inefficiency,ideal_gcmc,two_state_kmc,wham,block_summary)
from scripts.resource_estimator import estimate
class NumericalTests(unittest.TestCase):
    def test_force_is_energy_gradient(self):
        x=np.array([[1.,1.,1.],[2.2,1.1,1.],[1.,2.3,1.]])
        u,f,w=lj_forces(x,6.,2.)
        h=1e-6
        for i in range(len(x)):
            for d in range(3):
                xp=x.copy();xm=x.copy();xp[i,d]+=h;xm[i,d]-=h
                fd=-(lj_forces(xp,6.,2.)[0]-lj_forces(xm,6.,2.)[0])/(2*h)
                self.assertAlmostEqual(f[i,d],fd,places=6)
        np.testing.assert_allclose(f.sum(0),0,atol=1e-12)
    def test_cutoff_continuity(self):
        u,f=lj_pair(np.array([2.-1e-8,2.,2.1]),2.)
        np.testing.assert_allclose(u,0,atol=1e-12)
        np.testing.assert_allclose(f,0,atol=1e-7)
    def test_verlet_reversible(self):
        x,box=fcc(3,.75);rng=np.random.default_rng(9)
        v=rng.normal(scale=.15,size=x.shape);v-=v.mean(0)
        x0=x.copy();v0=v.copy();u,f,w=lj_forces(x,box,2.)
        for _ in range(20):x,v,f,u,w=velocity_verlet(x,v,f,box,.001,2.)
        v=-v
        for _ in range(20):x,v,f,u,w=velocity_verlet(x,v,f,box,.001,2.)
        np.testing.assert_allclose(x,x0,atol=1e-10)
        np.testing.assert_allclose(v,-v0,atol=1e-10)
    def test_energy_error_decreases(self):
        x0,box=fcc(3,.75);rng=np.random.default_rng(5)
        v0=rng.normal(scale=.3,size=x0.shape);v0-=v0.mean(0)
        def error(dt):
            x=x0.copy();v=v0.copy();u,f,w=lj_forces(x,box,2.)
            e0=u+.5*np.sum(v*v);err=[]
            for _ in range(round(.2/dt)):
                x,v,f,u,w=velocity_verlet(x,v,f,box,dt,2.)
                err.append(abs(u+.5*np.sum(v*v)-e0))
            return max(err)
        self.assertLess(error(.002),error(.004)*.5)
    def test_ideal_gas_rdf_same_and_cross(self):
        x=np.random.default_rng(5).uniform(0,10,size=(150,100,3))
        edges=np.linspace(.7,4.9,15)
        _,g=rdf(x,10,edges)
        _,gab=rdf(x,10,edges,np.arange(50),np.arange(50,100))
        np.testing.assert_allclose(g,1,atol=.075)
        np.testing.assert_allclose(gab,1,atol=.09)
    def test_ballistic_msd(self):
        t=np.arange(20)*.1;v=np.array([[1,2,0],[-1,0,2.]])
        x=t[:,None,None]*v[None,:,:]
        np.testing.assert_allclose(msd(x),5*t*t,atol=1e-12)
        np.testing.assert_allclose(msd(x,dimensions=(0,)),t*t,atol=1e-12)
    def test_known_diffusion_line(self):
        t=np.arange(20.);D=.4
        fitted,_=diffusion_slope(t,6*D*t+1,2,15,3)
        self.assertAlmostEqual(fitted,D)
    def test_ar1_correlation(self):
        rng=np.random.default_rng(10);x=np.empty(120000);x[0]=0
        for i in range(1,len(x)):x[i]=.8*x[i-1]+rng.normal()
        self.assertAlmostEqual(statistical_inefficiency(x[1000:]),9,delta=1.5)
    def test_block_accounting(self):
        s=block_summary(np.arange(103.),10)
        self.assertEqual(s["discarded_tail"],3);self.assertEqual(s["blocks"],10)
        self.assertAlmostEqual(s["mean"],49.5)
    def test_ideal_gcmc_poisson(self):
        n=ideal_gcmc(steps=180000,burn=5000,seed=15)
        self.assertAlmostEqual(n.mean(),5,delta=.15)
        self.assertAlmostEqual(n.var(),5,delta=.3)
    def test_kmc_time_weights(self):
        s,dt=two_state_kmc(tmax=10000,seed=4)
        self.assertAlmostEqual(dt.sum(),10000)
        self.assertAlmostEqual(np.sum(s*dt)/dt.sum(),2/3,delta=.015)
        self.assertAlmostEqual(s.mean(),.5,delta=.002)
    def test_wham_analytical_probabilities(self):
        x=np.linspace(-2,2,201);u=4*(x*x-1)**2;c=np.linspace(-1.5,1.5,13)
        w=6*(x[None,:]-c[:,None])**2
        h=np.exp(-u[None,:]-w);h=h/h.sum(1)[:,None]*10000
        p,_,_=wham(h,w)
        exact=np.exp(-u);exact/=exact.sum()
        np.testing.assert_allclose(p,exact,atol=2e-10)
    def test_disconnected_wham_rejected(self):
        with self.assertRaises(ValueError):wham([[5,0],[0,5]],[[0,1],[1,0]])
    def test_resource_arithmetic(self):
        r=estimate(1000,10,1,stride=100)
        self.assertEqual(r["steps_per_replica"],10000)
        self.assertEqual(r["frames_per_replica"],101)
        self.assertEqual(r["raw_coordinate_bytes_total"],1212000)
if __name__=="__main__":unittest.main()
