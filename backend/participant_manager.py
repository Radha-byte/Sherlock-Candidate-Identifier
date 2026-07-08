from backend.participant_models import Participant


class ParticipantManager:

    def __init__(self):
        self.participants = {}

    def add_participant(self, participant_id, display_name):

        if participant_id not in self.participants:

            self.participants[participant_id] = Participant(
                participant_id=participant_id,
                display_name=display_name
            )

    def get_participant(self, participant_id):

        return self.participants.get(participant_id)

    def get_all_participants(self):

        return list(self.participants.values())