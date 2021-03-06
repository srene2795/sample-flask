
import nomad
import sys

print sys.argv

job = {'Job': {'AllAtOnce': None,
  'Constraints': None,
  'CreateIndex': None,
  'Datacenters': ['dc1'],
  'ID': 'example4',
  'JobModifyIndex': None,
  'Meta': None,
  'ModifyIndex': None,
  'Name': 'example4',
  'Namespace': None,
  'ParameterizedJob': None,
  'ParentID': None,
  'Payload': None,
  'Periodic': None,
  'Priority': None,
  'Region': None,
  'Stable': None,
  'Status': None,
  'StatusDescription': None,
  'Stop': None,
  'SubmitTime': None,
  'TaskGroups': [{'Constraints': None,
    'Count': 1,
    'EphemeralDisk': {'Migrate': None, 'SizeMB': 300, 'Sticky': None},
    'Meta': None,
    'Name': 'cache',
    'RestartPolicy': {'Attempts': 10,
     'Delay': 25000000000,
     'Interval': 300000000000,
     'Mode': 'delay'},
    'Tasks': [{'Artifacts': None,
      'Config': {'command': 'sudo', 'args': ["sh","/home/deploy.sh",sys.argv[1]]},
      'Constraints': None,
      'DispatchPayload': None,
      'Driver': 'raw_exec',
      'Env': None,
      'KillTimeout': None,
      'Leader': False,
      'LogConfig': None,
      'Meta': None,
      'Name': 'python2'
      }],
    'Update': None}],
  'Type': 'batch',
  'VaultToken': None,
  'Version': None}}

my_nomad = nomad.Nomad(host='10.21.0.10')
response = my_nomad.job.register_job("example4", job)
