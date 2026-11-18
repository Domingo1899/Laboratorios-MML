# MML Labs — Matemática para Machine Learning (UCU)

Laboratorios de Matemática para Machine Learning (Universidad Católica del Uruguay), en Jupyter notebooks con Python.

## Laboratorios

| Notebook | Tema |
|---|---|
| `lab_1_1.ipynb` | Introducción al Álgebra Lineal con NumPy |
| `lab_1_2.ipynb` | Proyecciones Ortogonales, Gram-Schmidt y Descomposición QR |
| `lab_1_3.ipynb` | Autovalores, Autovectores y Métodos Iterativos |
| `lab_1_4.ipynb` | Costo Computacional, Precisión Numérica y Condicionamiento |
| `lab_2_1.ipynb` | Factorización de Matrices (LU y otras) |
| `lab_2_2.ipynb` | Descomposición en Valores Singulares (SVD) |
| `lab_3_2.ipynb` | Funciones Vectoriales, Jacobiano, Hessiana y Backpropagation |
| `lab_3_3.ipynb` | Integración Numérica |

Otros archivos:

- `ej1.4.7.py`: ejercicio 1.4.7 (polinomio característico con NumPy).
- `Untitled-1.ipynb`: borrador basado en el lab 1.1.
- `Bitacora_MML.pdf`: bitácora del curso.

## Librerías

- **NumPy**: álgebra lineal y cálculo numérico (todos los labs)
- **Matplotlib**: gráficos
- **SciPy**: factorizaciones (LU, QR, SVD) e integración
- **scikit-learn**: datasets en el lab 1.3
- **pandas** y **requests**: carga y descarga de datos en el lab 2.2
- **PyTorch**: diferenciación automática y backpropagation en el lab 3.2

## Cómo correrlos

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter lab
```
