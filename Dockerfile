FROM tensorflow/tensorflow:latest-gpu

WORKDIR /project

RUN pip install -U jupyterlab

EXPOSE 8888

ENTRYPOINT ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--no-browser", "--NotebookApp.token=''", "--NotebookApp.password=''"]
