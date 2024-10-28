# Template for a distribution helper

This Copier template helps to generate the necessary files to deploy a RayCluster with specific resources onto a K8S cluster for your application.

This template is based on [Ray's official documentation](https://docs.ray.io/en/latest/cluster/kubernetes/getting-started/raycluster-quick-start.html#kuberay-raycluster-quickstart).

## Generated files

```
├── Dockerfile                <- The Dockerfile to build the extended image that includes the necessary instructions for proper Ray Pods functionality.
├── build_N_publish_image.sh  <- The script that builds the image for the pods by extending the given base image and publishes it.
│
├── deploy.sh                 <- The script that deploys the desired resources onto the K8S cluster.
└── teardown.sh               <- The script that removes the deployment from the K8S cluster.
│
└── README.md                 <- The user guide.
```

Make sure to check `.../distributed_helper/README.md` for a user guide.