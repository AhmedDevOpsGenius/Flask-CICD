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

<img width="975" height="387" alt="image" src="https://github.com/user-attachments/assets/5cade0c4-18f1-48b6-956f-2891580ee29a" />

<img width="975" height="356" alt="image" src="https://github.com/user-attachments/assets/fc74540d-d4ef-40c7-9f2e-02a4f6fdf7ed" />



# CI/CD Pipeline

This pipeline automates the build, test, security scanning, and deployment of a Flask application to Kubernetes.

## Pipeline Overview

Tool: GitHub Actions

Language: Python (Flask)

Deployment: Docker + Helm

Stages: Security Scan → Test → Build → Image Scan → Push → Deploy

### 1. Security Scanning Stage
Static Application Security Testing (SAST)

Dependency Scanning

### 2. Test Stage

Run Python unit tests


### 3. Build Stage

Multi-stage Docker build:

Dockerfile linting:

Scan Docker image before pushing

Push image to DockerHub

<img width="1857" height="747" alt="image" src="https://github.com/user-attachments/assets/5b7e8665-8973-42d4-91c3-9d356cec4497" />


