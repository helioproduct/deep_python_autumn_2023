
#include <Python.h>
#include <stdio.h>

int fibonacci(int n) {
  if (n < 2) {
    return 1;
  }
  return fibonacci(n - 1) + fibonacci(n - 2);
}

PyObject *cutils_fibonacci(PyObject *self, PyObject *args) {
  int n;
  if (!PyArg_ParseTuple(args, "i")) {
    printf("failed to parse arguments");
    return NULL;
  }
  int res = fibonacci(n);
  return Py_BuildValue("i", res);
}

static PyMethodDef methods[] = {
    {"fibonacci", cutils_fibonacci, METH_VARARGS, "fibonacci"},
    {NULL, NULL, 0, NULL}};

static struct PyModuleDef cutilsmodule = {
    PyModuleDef_HEAD_INIT, "cutils_fibonacci", NULL, -1, methods};

PyMODINIT_FUNC PyInit_cutils(void) { return PyModule_Create(&cutilsmodule); }