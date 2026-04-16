#anomaly_labeling

def label_anomaly_score(score, red_thresh=0.6, yellow_thresh=0.3):
    """
    Assign anomaly label from combined score.
    """
    if score > red_thresh:
        return "red"
    if score > yellow_thresh:
        return "yellow"
    return "normal"


def label_block_scores(scores, red_thresh=0.6, yellow_thresh=0.3):
    """
    Label all scores in one block.
    """
    return [
        label_anomaly_score(score, red_thresh=red_thresh, yellow_thresh=yellow_thresh)
        for score in scores
    ]
