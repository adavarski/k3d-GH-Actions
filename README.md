### GitHub Actions k8s demo: k3d & helm
[![main](https://github.com/adavarski/k3d-GH-Actions/workflows/badge.svg)](https://github.com/adavarski/k3d-GH-Actions/actions)


K8s is Kubernetes. K3s is a lightweight K8s distribution. K3d is a wrapper to run K3s in Docker. K3d/K3s are especially good for development and CI purposes, as it takes only 20-30 seconds of time till the cluster is ready (for comparison, Kind/Minikube takes more time till ready)

### GitHub Actions configure
- Settings -> Developer settings -> Personal access tokens -> Create GHAT
- Repo Actions secrets and variables -> Add GHAT variable with value above PAT
- Repo Settings -> Actions -> Genreal -> Workflow permissions -> Check Read and write permissions & Allow GH Actions to approve PR

GH Actions workflow: Test Python Code -> Build/Push Image ->  Deploy/Test Helm Chart on K8s -> Update Helm Chart (Image Tag -> for example: ArgoCD to use it: `infra repo:helm charts` and do CD -> Ref: https://github.com/adavarski/ArgoCD-GitOps-playground && https://github.com/adavarski/homelab
