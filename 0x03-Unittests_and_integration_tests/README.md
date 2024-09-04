# 0x03. Unittests and Integration Tests
![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/1/f088970b450e82c881ea.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20240904%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240904T055054Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=ed969d71bd9610af35e689e5b603ea30367abe789c5371d94c98e24dc31237c9)

Unit testing is the process of testing that a particular function returns expected results for different set of inputs. A unit test is supposed to test standard inputs and corner cases. A unit test should only test the logic defined inside the tested function. Most calls to additional functions should be mocked, especially if they make network or database calls.

The goal of a unit test is to answer the question: if everything defined outside this function works as expected, does this function work as expected?

Integration tests aim to test a code path end-to-end. In general, only low level functions that make external calls such as HTTP requests, file I/O, database I/O, etc. are mocked.

Integration tests will test interactions between every part of your code.

Execute your tests with

```
$ python -m unittest path/to/test_file.py
```

## Resources

**Read or watch:**

-   [unittest — Unit testing framework](https://intranet.alxswe.com/rltoken/a_AEObGK8jeqPtTPmm-gIA "unittest — Unit testing framework")
-   [unittest.mock — mock object library](https://intranet.alxswe.com/rltoken/PKetnACd7FfRiU8_kpe5EA "unittest.mock — mock object library")
-   [How to mock a readonly property with mock?](https://intranet.alxswe.com/rltoken/2ueVPK1kWZuz525FvZ1v2Q "How to mock a readonly property with mock?")
-   [parameterized](https://intranet.alxswe.com/rltoken/mI7qc3Y42aZ7GTlLXDxgEg "parameterized")
-   [Memoization](https://intranet.alxswe.com/rltoken/x83Hdr54q4Vax5xQ2Z3HSA "Memoization")

## Learning Objectives

At the end of this project, you are expected to be able to [explain to anyone](https://intranet.alxswe.com/rltoken/NfT-nNKrNHGrDMY-Qm-1Dg "explain to anyone"), **without the help of Google**:

-   The difference between unit and integration tests.
-   Common testing patterns such as mocking, parametrizations and fixtures

## Requirements

-   All your files will be interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7)
-   All your files should end with a new line
-   The first line of all your files should be exactly `#!/usr/bin/env python3`
-   A `README.md` file, at the root of the folder of the project, is mandatory
-   Your code should use the `pycodestyle` style (version 2.5)
-   All your files must be executable
-   All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
-   All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
-   All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
-   A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
-   All your functions and coroutines must be type-annotated.

## Required Files

### `utils.py` (or [download](https://intranet-projects-files.s3.amazonaws.com/webstack/utils.py "download"))

Click to show/hide file contents

```

#!/usr/bin/env python3
"""Generic utilities for github org client.
"""
import requests
from functools import wraps
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)

__all__ = [
    "access_nested_map",
    "get_json",
    "memoize",
]


def access_nested_map(nested_map: Mapping, path: Sequence) -&gt; Any:
    """Access nested map with key path.
    Parameters
    ----------
    nested_map: Mapping
        A nested map
    path: Sequence
        a sequence of key representing a path to the value
    Example
    -------
    &gt;&gt;&gt; nested_map = {"a": {"b": {"c": 1}}}
    &gt;&gt;&gt; access_nested_map(nested_map, ["a", "b", "c"])
    1
    """
    for key in path:
        if not isinstance(nested_map, Mapping):
            raise KeyError(key)
        nested_map = nested_map[key]

    return nested_map


def get_json(url: str) -&gt; Dict:
    """Get JSON from remote URL.
    """
    response = requests.get(url)
    return response.json()


def memoize(fn: Callable) -&gt; Callable:
    """Decorator to memoize a method.
    Example
    -------
    class MyClass:
        @memoize
        def a_method(self):
            print("a_method called")
            return 42
    &gt;&gt;&gt; my_object = MyClass()
    &gt;&gt;&gt; my_object.a_method
    a_method called
    42
    &gt;&gt;&gt; my_object.a_method
    42
    """
    attr_name = "_{}".format(fn.__name__)

    @wraps(fn)
    def memoized(self):
        """"memoized wraps"""
        if not hasattr(self, attr_name):
            setattr(self, attr_name, fn(self))
        return getattr(self, attr_name)

    return property(memoized)
```

### `client.py` (or [download](https://intranet-projects-files.s3.amazonaws.com/webstack/client.py "download"))

Click to show/hide file contents

```

#!/usr/bin/env python3
"""A github org client
"""
from typing import (
    List,
    Dict,
)

from utils import (
    get_json,
    access_nested_map,
    memoize,
)


class GithubOrgClient:
    """A Githib org client
    """
    ORG_URL = "https://api.github.com/orgs/{org}"

    def __init__(self, org_name: str) -&gt; None:
        """Init method of GithubOrgClient"""
        self._org_name = org_name

    @memoize
    def org(self) -&gt; Dict:
        """Memoize org"""
        return get_json(self.ORG_URL.format(org=self._org_name))

    @property
    def _public_repos_url(self) -&gt; str:
        """Public repos URL"""
        return self.org["repos_url"]

    @memoize
    def repos_payload(self) -&gt; Dict:
        """Memoize repos payload"""
        return get_json(self._public_repos_url)

    def public_repos(self, license: str = None) -&gt; List[str]:
        """Public repos"""
        json_payload = self.repos_payload
        public_repos = [
            repo["name"] for repo in json_payload
            if license is None or self.has_license(repo, license)
        ]

        return public_repos

    @staticmethod
    def has_license(repo: Dict[str, Dict], license_key: str) -&gt; bool:
        """Static: has_license"""
        assert license_key is not None, "license_key cannot be None"
        try:
            has_license = access_nested_map(repo, ("license", "key")) == license_key
        except KeyError:
            return False
        return has_license
```

### `fixtures.py` (or [download](https://intranet-projects-files.s3.amazonaws.com/webstack/fixtures.py "download"))

Click to show/hide file contents