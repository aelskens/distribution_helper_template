#!/bin/bash

helm uninstall -n ray raycluster
helm uninstall -n ray kuberay-operator