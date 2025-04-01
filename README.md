# How to deploy source-to-image application

## Getting started

### How to deploy application on Openshift using s2i

```sh
oc new-app https://github.com/taisyo7333/s2i-python-example.git --strategy=source
```

### How to track BuildConfig's progres

You will see the following message on yourteminal how to track its progress.

```sh
oc logs -f buildconfig/s2i-python-example
```

### How to see it's status

```sh
os status
```

### How to update the application

```sh
oc start-build s2i-python-example
```

### How to delete the application

```sh
oc delete all -l app=s2i-python-example
```

## Reference

* [S2I Pytyon](https://docs.redhat.com/en/documentation/openshift_online/3/html-single/using_images/index#overview-4)
* [S2I Requirements](https://docs.redhat.com/en/documentation/openshift_online/3/html-single/creating_images/index#overview-3)
* [How to crate an S2I Builder Image](https://www.redhat.com/en/blog/create-s2i-builder-image)
* [How to deploy application on Openshift](https://docs.redhat.com/en/documentation/openshift_online/3/html-single/developer_guide/index#dev-guide-index)
* [GitHub - Source to Image](https://github.com/openshift/source-to-image)
* [GitHub - s2i-python-container](https://github.com/sclorg/s2i-python-container/tree/master)
* https://rheb.hatenablog.com/entry/running-s2i-locally
