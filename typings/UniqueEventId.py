class UniqueEventId(str):
    def __new__(cls, world_id: int, instance_id: int):
        new_event_id = f'{world_id}-{instance_id}'
        return super().__new__(cls, new_event_id)
