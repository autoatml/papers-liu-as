from jobflow import Flow
from autoplex.auto.rss.flows import RssMaker
from fireworks import LaunchPad
from jobflow.managers.fireworks import flow_to_workflow


job = RssMaker().make(config_file='/path/to/rss_as_config.yaml')
flow = Flow([job], output=job.output)
wf = flow_to_workflow(flow) 
lpad = LaunchPad.auto_load()
lpad.add_wf(wf)
