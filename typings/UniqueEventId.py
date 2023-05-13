class UniqueEventId:
    def __init__(self, world_id: int, instance_id: int) -> None:
        """Combines world_id and instance_id to create a unique event id

        Args:
            - world_id: `int` Event world_id
            - instance_id: `int` Event instance_id
        """
        self.world_id = world_id
        self.instance_id = instance_id

    def __str__(self) -> str:
        return f'{self.world_id}-{self.instance_id}'
    
    def __repr__(self) -> str:
        return f'UniqueEventId(world_id={self.world_id}, instance_id={self.instance_id})'
