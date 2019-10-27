"""
Misc functions to clean up main file
"""
from typing import List
from yaml import safe_load
from configparser import ConfigParser


def deep_search(haystack: dict, keypath: List[str]):
    """
    If path = ["foo", "bar", "baz"]
    The assumed values are:
    haystack = {
        foo: {
            bar: {
                baz: {}
            }
        }
    }
    Where the dict that baz points to is returned

    If this is not the case, the config haystack is modified
    in order to facilitate this
    """
    if not isinstance(haystack, dict):
        raise TypeError()
    if not isinstance(keypath, list):
        raise TypeError()
    to_search = haystack
    for item in keypath:
        if item not in to_search:
            # to_search[item] is not set, create dict and continue
            to_search[item] = {}
            to_search = to_search[item]
            continue
        intermediary = to_search[item]
        if not isinstance(intermediary, dict):
            # Intermediary is a value, replace with a dict
            del to_search[item]
            to_search[item] = {}
        to_search = to_search[item]
    return to_search


def yaml_to_dict(filepath: str):
    try:
        with open(filepath, 'r') as yml_config:
            return safe_load(yml_config)
    except Exception:
        return None


def prop_to_dict(filepath: str):
    # try:
    with open(filepath, 'r') as prop_config:
        config = ConfigParser()
        config.read_string(
            '[config]\n' + prop_config.read())
        return dict(config.items('config'))
    # except Exception:
    #     return None
