=======
Testing
=======

.. _unit-tests:

Unit Tests
----------

To run all unit tests:

.. code-block:: console

  $ nosetests --verbosity=2 test/unit/*

To run all unit tests in a single file:

.. code-block:: console

  $ nosetests --verbosity=2 test/unit/path/to/test_file.py


To run a single unit test:

.. code-block:: console

  $ nosetests --verbosity=2 test/unit/path/to/test_file.py:test_x_y_and_z.py


Add unit tests for ``culturemesh/path/to/file.py`` at
``test/unit/path/to/file/test_file.py``.

    .. note:: At the moment we unit test only
        the ``client`` class.  To ease development, we initially created a 'mock'
        client that returns fake API data from ``data/``, and we use this for
        unit testing. In the future, these tests should be updated to use
        the ``mock`` library and the 'mock' client should be deprecated.

.. _integ-tests:

Integration Tests
-----------------

There are currently no integration tests for CultureMesh FFB.
