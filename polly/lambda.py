import boto3

Polly = boto3.client('polly')

try:
    speechTask = Polly.start_speech_synthesis_task(
        OutputFormat='mp3',
        OutputS3BucketName='table21-polly-output',
        OutputS3KeyPrefix='0123456789-oasdsf',
        SampleRate='8000',
        Text='Bonjour, c\'est un premier test de traduction',
        TextType='text',
        VoiceId='Mathieu'
    )

    speechTaskStatus = speechTask['SynthesisTask']['TaskStatus']

    while speechTaskStatus != 'completed':
        response = Polly.get_speech_synthesis_task(
            TaskId=speechTask['SynthesisTask']['TaskId']
        )
        speechTaskStatus = response['SynthesisTask']['TaskStatus']

    print(speechTask['SynthesisTask']['OutputUri'])
except:
    print(False)
