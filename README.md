# AWS CLI plugin for tailing CloudWatch Logs

An awscli plugin backporting the [tail command](https://github.com/aws/aws-cli/pull/3729) from AWS CLI v2

## AWS CLI Tail Command

This plugin is a backport of the [tail command](https://github.com/aws/aws-cli/pull/3729) added in AWS CLI v2.

## Installation

To install the latest release of the logs tail plugin:


```
$ pip install awscli-plugin-logs-tail

```

To install the plugin from source:

```
$ pip install git+https://github.com/corymbia/logs-tail-awscli-plugin.git
```

This requires `pip` and `git` are available.

## Configuration

To enable the plugin:

```
$ cat .aws/config 
[plugins]
logs_tail = awscli_plugin_logs_tail
```

## Usage

Assuming the plugin is registered:

```
$ aws logs tail LOG_GROUP_NAME
...
...
```

See command help for details:

```
$ aws logs tail help
```
