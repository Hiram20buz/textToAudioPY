### How to solve

Note: This error originates from the build backend, and is likely not a problem with poetry but with playsound (1.3.0) not supporting PEP 517 builds. You can verify this by running 'pip wheel --no-cache-dir --use-pep517 "playsound (==1.3.0)"'.



https://pythonfix.com/pkg/p/playsound/


https://github.com/TaylorSMarks/playsound/issues/148


pip install playsound@git+https://github.com/taconi/playsound


poetry add playsound@git+https://github.com/taconi/playsound
