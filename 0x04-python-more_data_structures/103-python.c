#include "/usr/include/python3.4/Python.h"
#include <stdio.h>

void print_hexn(const char *str, int n)
{
	int i = 0;

	for (; i < n - 1; ++i)
		printf("%02x ", (unsigned char) str[i]);

	printf("%02x", str[i]);
}

void print_python_bytes(PyObject *p)
{
	PyBytesObject *clone = (PyBytesObject *) p;
	int bytes_num, size_copy = 0;

	printf("[.] bytes object info\n");
	if (PyBytes_Check(clone))
	{
		size_copy = PyBytes_Size(p);
		bytes_num = size_copy + 1;

		if (bytes_num >= 10)
			bytes_num = 10;

		printf("  size: %d\n", size_copy);
		printf("  trying string: %s\n", clone->ob_sval);
		printf("  first %d bytes: ", bytes_num);
		print_hexn(clone->ob_sval, bytes_num);
		printf("\n");
	}
	else
	{
		printf("  [ERROR] Invalid Bytes Object\n");
	}
}

void print_python_list(PyObject *p)
{
	int i = 0, len_list = 0;
	PyObject *item;
	PyListObject *clone = (PyListObject *) p;

	printf("[*] Python list info\n");
	len_list = PyList_GET_SIZE(p);
	printf("[*] Size of the Python List = %d\n", len_list);
	printf("[*] Allocated = %d\n", (int) clone->allocated);

	for (; i < len_list; ++i)
	{
		item = PyList_GET_ITEM(p, i);
		printf("Element %d: %s\n", i, item->ob_type->tp_name);

		if (PyBytes_Check(item))
			print_python_bytes(item);
	}
}
