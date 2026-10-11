"""Arithmetic planning, not a performance benchmark."""
import argparse,json,math
def estimate(atoms,duration_ps,dt_fs,stride=100,bytes_per_scalar=4,arrays=1,
             seconds_per_step=None,replicas=1):
    if min(atoms,duration_ps,dt_fs,stride,bytes_per_scalar,arrays,replicas)<=0:
        raise ValueError("All size and duration inputs must be positive.")
    steps=math.ceil(duration_ps*1000/dt_fs)
    frames=steps//stride+1
    out={"steps_per_replica":steps,"frames_per_replica":frames,
         "raw_coordinate_bytes_total":replicas*frames*atoms*3*bytes_per_scalar*arrays,
         "assumptions":"Fixed output stride; initial frame; no headers/compression/topology/checkpoints; arrays includes coordinates and optionally velocities/forces."}
    if seconds_per_step is not None:
        if seconds_per_step<=0:raise ValueError("Measured seconds/step must be positive.")
        out["projected_wall_hours_per_replica"]=steps*seconds_per_step/3600
        out["summed_replica_wall_hours"]=replicas*steps*seconds_per_step/3600
    return out
def main():
    p=argparse.ArgumentParser()
    p.add_argument("--atoms",type=int,required=True);p.add_argument("--duration-ps",type=float,required=True)
    p.add_argument("--dt-fs",type=float,required=True);p.add_argument("--stride",type=int,default=100)
    p.add_argument("--bytes-per-scalar",type=int,default=4);p.add_argument("--arrays",type=int,default=1)
    p.add_argument("--replicas",type=int,default=1);p.add_argument("--seconds-per-step",type=float)
    a=p.parse_args();print(json.dumps(estimate(**vars(a)),indent=2))
if __name__=="__main__":main()
