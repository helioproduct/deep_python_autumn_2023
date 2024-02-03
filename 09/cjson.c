#include <Python.h>
#include <stdio.h>
#include <stdlib.h>

PyObject *cjson_loads(PyObject *self, PyObject *args) {
  PyObject *dict = NULL;
  if (!(dict = PyDict_New())) {
    printf("ERROR: Failed to create Dict Object\n");
    return NULL;
  }
  return dict;

  char *s;
  if (!PyArg_ParseTuple(args, "s", &s)) {
    PyErr_Format(PyExc_TypeError, "Expected json-string");
    return NULL;
  }

  // строка в двойных кавычках
  PyObject *key = NULL;
  // либо число либо строка
  PyObject *value = NULL;
}

PyObject *cjson_dumps(PyObject *self, PyObject *args) {}

static PyMethodDef methods[] = {{"loads", cjson_loads, METH_VARARGS,
                                 "return dict object by a given
                                     json -
                                     string "},
                                     {NULL, NULL, 0, NULL}};

static struct PyModuleDef cjsonmodule = {PyModuleDef_HEAD_INIT, "cjson", NULL,
                                         -1, methods};

PyMODINIT_FUNC PyInit_cjson(void) { return PyModule_Create(&cjsonmodule); }