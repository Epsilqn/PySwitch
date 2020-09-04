# PySwitch

![GitHub top language](https://img.shields.io/github/languages/top/Epsilqn/PySwitch)
![GitHub language count](https://img.shields.io/github/languages/count/Epsilqn/PySwitch)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/Epsilqn/PySwitch)
![GitHub repo size](https://img.shields.io/github/repo-size/Epsilqn/PySwitch)
![GitHub All Releases](https://img.shields.io/github/downloads/Epsilqn/PySwitch/total)
![GitHub issues](https://img.shields.io/github/issues/Epsilqn/PySwitch)
![GitHub](https://img.shields.io/github/license/Epsilqn/PySwitch)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/Epsilqn/PySwitch?sort=semver)
![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/Epsilqn/PySwitch?include_prereleases&label=pre-release&sort=semver)

PySwitch is the smallest and simplest library for implementing switch statements in Python. No more manual dictionaries! Just import PySwitch and optimize your code.

## Installation

### Prerequisites

* Python 3.6+

## Usage

```py
from switch import Switch


def my_default_function(): print("Default executed")
def _1(): print("Function 1 executed")
def _2(): print("Function 2 executed")


my_switch = Switch(my_default_function)
my_switch.add("1", _1)
my_switch.add("2", _2)
my_switch.exec(input("Execute: "))
```
