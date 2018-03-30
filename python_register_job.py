
import nomad

job = {'Job': {'AllAtOnce': None,
  'Constraints': None,
  'CreateIndex': None,
  'Datacenters': ['dc1'],
  'ID': 'example3',
  'JobModifyIndex': None,
  'Meta': None,
  'ModifyIndex': None,
  'Name': 'example3',
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
      'Config': {'command': 'sudo', 'args': ["python","/home/srene-test/Hello.py"]},
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
  'Type': 'service',
  'VaultToken': None,
  'Version': None}}

my_nomad = nomad.Nomad(host='10.21.0.10')
response = my_nomad.job.register_job("example3", job)