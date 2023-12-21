def remove_repetitions(transcription, sequence_length=1):
    words = transcription.split()
    cleaned_transcription = []
    seen_sequences = set()

    for i in range(len(words) - sequence_length + 1):
        sequence = ' '.join(words[i:i + sequence_length])
        if sequence not in seen_sequences:
            cleaned_transcription.extend(words[i:i + sequence_length])
            seen_sequences.add(sequence)

    return ' '.join(cleaned_transcription)
