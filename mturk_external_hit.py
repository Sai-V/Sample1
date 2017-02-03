import boto.mturk.connection
import boto.mturk.question

sandbox_host = 'mechanicalturk.sandbox.amazonaws.com'
real_host = 'mechanicalturk.amazonaws.com'

mturk = boto.mturk.connection.MTurkConnection(
    aws_access_key_id = 'AKIAJN3NC726HKVYAMHQ',
    aws_secret_access_key = '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',
    host = sandbox_host,
    debug = 1 # debug = 2 prints out all requests. but we'll just keep it at 1
)

print boto.Version
print mturk.get_account_balance()


URL = "https://sai-v.github.io/Sample1/"
title = "A special hit!"
description = "The more verbose description of the job!"
keywords = ["cats", "dogs", "rabbits"]
frame_height = 500 # the height of the iframe holding the external hit
amount = 0


questionform = boto.mturk.question.ExternalQuestion( URL, frame_height )

create_hit_result = mturk.create_hit(
    title = title,
    description = description,
    keywords = keywords,
    question = questionform,
    reward = boto.mturk.price.Price( amount = amount),
    response_groups = ( 'Minimal', 'HITDetail' ), # I don't know what response groups are
    )

HIT = create_hit_result[0]
assert create_hit_result.status

print '[create_hit( %s, $%s ): %s]' % ( URL, amount, HIT.HITId )
