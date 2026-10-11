"""Execute course notebooks: standard kernels, or socket-free cell execution.
The inprocess mode is explicit and recorded; it does not test Jupyter messaging.
"""
import argparse,json,contextlib,io,base64
from pathlib import Path
import nbformat
def inprocess(nb):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    namespace={"__name__":"__main__"}
    count=0
    for cell in nb.cells:
        if cell.cell_type!="code":continue
        count+=1;cell.outputs=[];cell.execution_count=count
        def show(*args,**kwargs):
            for num in plt.get_fignums():
                fig=plt.figure(num);buf=io.BytesIO();fig.savefig(buf,format="png",dpi=110,bbox_inches="tight")
                cell.outputs.append(nbformat.v4.new_output("display_data",data={"image/png":base64.b64encode(buf.getvalue()).decode(),"text/plain":"Matplotlib teaching figure"}))
            plt.close("all")
        plt.show=show
        stream=io.StringIO()
        with contextlib.redirect_stdout(stream),contextlib.redirect_stderr(stream):
            exec(compile(cell.source,"<notebook-cell>","exec"),namespace)
        if stream.getvalue():cell.outputs.insert(0,nbformat.v4.new_output("stream",name="stdout",text=stream.getvalue()))
    nb.metadata["course_execution_mode"]="inprocess: fresh namespace per notebook; code and figures executed; Jupyter transport not tested"
def main():
    p=argparse.ArgumentParser();p.add_argument("--output",type=Path,default=Path("outputs/executed_notebooks"))
    p.add_argument("--mode",choices=["kernel","inprocess"],default="kernel")
    a=p.parse_args();root=Path(__file__).resolve().parents[1];a.output.mkdir(parents=True,exist_ok=True)
    report=[]
    for path in sorted((root/"notebooks").glob("*.ipynb")):
        nb=nbformat.read(path,as_version=4);nbformat.validate(nb)
        if a.mode=="kernel":
            from nbclient import NotebookClient
            NotebookClient(nb,timeout=240,kernel_name="python3",resources={"metadata":{"path":str(root)}}).execute()
        else:inprocess(nb)
        nbformat.write(nb,a.output/path.name)
        report.append({"notebook":path.name,"code_cells":sum(c.cell_type=="code" for c in nb.cells),
                       "status":"executed without error","mode":a.mode})
        print(path.name,"PASS",a.mode,flush=True)
    (a.output/"execution_report.json").write_text(json.dumps(report,indent=2)+"\n")
if __name__=="__main__":main()
