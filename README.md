# Creating a basic S2I builder image

## Getting started

### How to deploy application on Openshift using s2i

```sh
oc new-app https://github.com/taisyo7333/s2i-python-test.git --strategy=source
```

### How to track BuildConfig's progres

You will see the following message on yourteminal how to track its progress.

```sh
oc logs -f buildconfig/s2i-python-test
```

### How to see it's status

```sh
os status
```

### How to update the application

```sh
oc start-build s2i-python-test
```

