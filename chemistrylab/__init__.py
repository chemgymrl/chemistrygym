'''
ChemistryLab Init Registration File

:title: __init__.py

:author: Chris Beeler and Mitchell Shahen

:history: 2020-07-03
'''

from gym.envs.registration import register

############################ ExtractBench ####################################

register(
    id='GenWurtzExtract-v2',
    entry_point='chemistrylab.general_bench.extract_bench_v1:GeneralWurtzExtract_v2',
)

############################ ReactBench ####################################

register(
    id='GenWurtzReact-v2',
    entry_point='chemistrylab.general_bench.reaction_bench_v1:GeneralWurtzReact_v2'
)

register(
    id='FictReact-v2',
    entry_point='chemistrylab.general_bench.reaction_bench_v1:FictReact_v2'
)


############################ DistillationBench ####################################

register(
    id='GenWurtzDistill-v2',
    entry_point='chemistrylab.general_bench.distillation_bench_v1:GeneralWurtzDistill_v2',
    max_episode_steps=100
)

############################ LabManager ####################################

register(
    id='LabManager-v0',
    entry_point='chemistrylab.manager.manager_v1:LabManager',
    max_episode_steps=100
)
