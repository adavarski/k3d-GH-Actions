### GitHub Actions k8s demo: k3d & helm

K8s is Kubernetes. K3s is a lightweight K8s distribution. K3d is a wrapper to run K3s in Docker. K3d/K3s are especially good for development and CI purposes, as it takes only 20-30 seconds of time till the cluster is ready (for comparison, Kind/Minikube takes more time till ready)

### GitHub Actions configure
- Settings -> Developer settings -> Personal access tokens -> Create ARGOCD 
- Repo Actions secrets and variables -> Add ARGOCD variable with value above PAT
- Repo Settings -> Actions -> Genreal -> Workflow permissions -> Check Read and write permissions & Allow GH Actions to approve PR

GH Actions workflow: Test Python Code -> Build/Push Image ->  Deploy/Test Helm Chart on K8s -> Update Helm Chart (Image Tag -> for example: feature ArgoCD usage -> Ref: https://github.com/adavarski/ArgoCD-GitOps-playground) 
