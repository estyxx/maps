import subprocess
import webbrowser


def start_notebook():
    notebook_path = "Emilia_Romagna_Provinces_Map.ipynb"

    # Start the Jupyter Notebook server
    subprocess.Popen(["poetry", "run", "jupyter", "notebook", notebook_path])

    # Open the notebook in the default web browser
    webbrowser.open(f"http://localhost:8888/notebooks/{notebook_path}")


if __name__ == "__main__":
    start_notebook()
