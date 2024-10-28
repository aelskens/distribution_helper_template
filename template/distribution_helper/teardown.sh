#!/bin/bash

helm uninstall -n distributed-ray raycluster
helm uninstall -n distributed-ray kuberay-operator