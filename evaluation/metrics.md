# Evaluation

## Testing Methodology

The prototype was evaluated using a simulated interview dataset consisting of multiple meeting participants with different behaviors.

The system processes meeting events sequentially to simulate a real-time interview environment.

Each participant generates evidence throughout the meeting, and the confidence score is continuously updated as new information becomes available.

The following evidence sources were evaluated:

- Metadata Matching
- Camera Activity
- Face Recognition
- Voice Recognition
- Transcript Analysis
- Speaking Duration

The final prediction is made by combining all available evidence instead of relying on a single rule.

---

# Test Scenario

### Registered Candidate

Rahul Sharma

### Participants

| Participant | Display Name |
|-------------|--------------|
| P1 | MacBook Pro |
| P2 | John HR |
| P3 | Observer |
| P4 | Guest User |

Initially, the candidate joined using the device name **MacBook Pro** instead of the actual name.

During the interview, additional evidence became available through transcript, camera activity, voice recognition, face recognition and speaking duration.

The confidence score gradually increased until the participant was identified with high confidence.

---

# Results

| Metric | Result |
|---------|--------|
| Participants Tested | 4 |
| Correct Candidate Identified | Yes |
| Final Confidence | 100% |
| Real-Time Confidence Updates | Supported |
| Evidence Explanation | Supported |
| Candidate Ranking | Supported |

---

# Edge Cases Tested

## 1. Candidate joins using device name

Example:

MacBook Pro

Result:

Metadata alone provides low confidence initially.

Face recognition, transcript analysis and voice recognition gradually increase confidence.

Status:

PASS

---

## 2. Multiple Interviewers

Several interviewers can join the meeting simultaneously.

The system avoids selecting them because they lack sufficient candidate-related evidence.

Status:

PASS

---

## 3. Silent Observer

An observer joins but never speaks.

The participant receives very little confidence due to missing evidence.

Status:

PASS

---

## 4. Missing Metadata

Even if display names are incorrect, the system continues using transcript, face recognition, voice recognition and speaking activity.

Status:

PASS

---

## 5. Ambiguous Participants

When multiple participants share similar characteristics, the system assigns confidence scores to all participants instead of making an immediate hard decision.

The highest confidence participant is selected.

Status:

PASS

---

# Accuracy

For the simulated interview dataset used in this prototype,

Candidate Identification Accuracy:

**100% (1 out of 1 interview scenario)**

Since this is a proof-of-concept prototype, larger datasets are required for statistically meaningful evaluation.

---

# Limitations

- Uses simulated meeting events instead of live Google Meet or Zoom streams.
- Face and voice recognition modules are rule-based placeholders rather than production deep-learning models.
- No deepfake detection.
- No active speaker diarization.
- No real-time webcam processing.
- No live microphone processing.
- Limited evaluation dataset.

---

# Future Improvements

- Integrate live Google Meet and Microsoft Teams APIs.
- Replace simulated face matching with FaceNet or InsightFace.
- Replace simulated voice matching with ECAPA-TDNN speaker embeddings.
- Add deepfake detection.
- Add gaze tracking and behavioral analysis.
- Train confidence fusion using machine learning instead of manually assigned scores.
- Evaluate using a large-scale interview dataset.

---

# Conclusion

The prototype successfully demonstrates how multiple weak evidence signals can be fused to identify the interview candidate in real time.

Instead of relying on a single feature, the system continuously updates confidence, explains every decision, and gracefully handles uncertainty, making it suitable as a proof-of-concept for Sherlock AI's candidate identification pipeline.