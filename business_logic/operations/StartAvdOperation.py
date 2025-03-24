from business_logic.generic_operation import GenericOperation
    from business_logic.operations_registry import register_operation

    @register_operation("START_AVD")
    class StartAvdOperation(GenericOperation):
        """
        This operation will look for the environment variable START_AVD_CONFIG_YAML,
        then inside that YAML file, it will find the key 'start_avd' and read steps_order, steps, etc.

        For example, if START_AVD_CONFIG_YAML=/path/to/start_avd.yaml,
        it will load that file and expect something like:

            start_avd:
            record_final_state: true
            ...
            steps_order:
                ...
            steps:
                ...
        """

        def get_operation_name(self) -> str:
            # Tells the GenericOperation to look inside raw_config["start_avd"] in your YAML
            return "start_avd"
    