FROM continuumio/miniconda3:24.7.1-0

COPY environment.yml .
RUN conda env create -f environment.yml

# Activate the Conda environment
RUN echo "conda activate geog213-final" >> ~/.bashrc
ENV PATH="$PATH:/opt/conda/envs/geog213-final/bin"

# Create a non-root user and switch to that user
RUN useradd -m user
USER user

WORKDIR /home/user
COPY --chown=user geog213_phillips_report.ipynb .
COPY --chown=user utils.py .

# Expose the JupyterLab port
EXPOSE 8888

EXPOSE 8787

# Start JupyterLab
CMD ["jupyter", "lab", "--ip=0.0.0.0"]
