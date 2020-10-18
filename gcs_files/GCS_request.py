def transcribe_gcs(gcs_uri):
    """Asynchronously transcribes the audio file specified by the gcs_uri."""
    from google.cloud import speech

    client = speech.SpeechClient()

    audio = speech.RecognitionAudio(uri=gcs_uri)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.FLAC,
        sample_rate_hertz=16000,
        language_code="en-US",
    )

    operation = client.long_running_recognize(
        request={"config": config, "audio": audio}
    )

    operation = client.long_running_recognize(config=config, audio=audio)

    print("Waiting for operation to complete...")
    response = operation.result(timeout=90)

    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    for result in response.results:
        # The first alternative is the most likely one for this portion.
        trans = u"{}".format(result.alternatives[0].transcript)

        with open("%s.txt" % name, "w") as text_file:
            text_file.write(trans)
        #print("Confidence: {}".format(result.alternatives[0].confidence))
    
my_file = open('YAF_angry/file_list.txt')   # file name list directory
all_the_lines = my_file.readlines()

items = []
for i in all_the_lines:
    items.append(i)

new_items = [x[:-1] for x in items]

for name in new_items:  
    transcribe_gcs("gs://comp8240_tess/flac/" + name + ".flac")   # cloud storage files with location
