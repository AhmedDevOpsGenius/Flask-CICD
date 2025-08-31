# Flask-CICD
# Kubernetes & CI/CD Setup Documentation

This repository contains instructions and files to set up a single-node Kubernetes cluster and a CI/CD pipeline for a Flask application. It also includes screenshots demonstrating the running cluster and pipeline.


Kubernetes Setup (Manual)
Prerequisites

Local VM running CentOS 7 / Ubuntu 20.04.

Docker / containerd installed.

Kubeadm, kubectl, kubelet installed.

Minimum 2 CPUs, 2GB RAM, 20GB disk space.

Cluster Setup

Initialize Kubernetes cluster using kubeadm:

sudo kubeadm init --pod-network-cidr=192.168.0.0/16


Configure kubectl for the admin user:

mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config


Install Calico CNI for networking:

kubectl apply -f https://docs.projectcalico.org/manifests/calico.yaml


<img width="975" height="781" alt="image" src="https://github.com/user-attachments/assets/352344f1-0d8d-4c89-ac7e-5f033efdc752" />

