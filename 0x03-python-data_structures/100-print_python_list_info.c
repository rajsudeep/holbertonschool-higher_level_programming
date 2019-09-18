#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - prints basic info about a pyobject
 * @p: a python object
 */
void print_python_list_info(PyObject *p)
{
	int i;
	PyObject *obj;

	printf("[*] Size of the Python List = %i\n", Py_SIZE(p));
	printf("[*] Allocated = %zd\n", ((PyListObject *) p)->allocated);
	for (i = 0; i < Py_SIZE(p); i++)
	{
		obj = PyList_GetItem(p, i);
		printf("Element %i: %s\n", i, Py_TYPE(obj)->tp_name);
	}
}
