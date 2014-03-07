# coding=UTF8

environ = {
    "default": {
        "root": "http://localhost:5000",
        "headers": {'Accept': 'application/json', 'Content-type': 'application/json'}
    },
    "env00": {
        "root": "http://localhost:5000"
    },
    "complete": {
        "root": "http://localhost:5000",
        "headers": {'Accept': 'application/json', 'Content-type': 'application/json'}
    }
}

data = {
    "login": {
        "email": "iolivie@rielcano.org",
        "password": "iolivie@rielcano.org"
    }
}

output = {
    "login": {
        "uu": "kk",
        "jj": "pp"
    }
}

test = {
    "module": "module",
    "tests": {
        "t00": {
            "name": "Get session",
            "environ": "env00",
            "method": "get",
            "url": "/usr/login",
            "data": "login",
            "output": "login"
        },
        "t01": {
            "name": "Test 01",
            "callback": "test01"
        },
        "complete": {
            "name": "name",
            "method": "method",
            "url": "/usr/login",
            "data": "login",
            "output": "login",
            "callback": "test02",
            "environ": "environ"
        }
    }
}
