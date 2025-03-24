from business_logic.generic_operation import GenericOperation
    from business_logic.operations_registry import register_operation

    @register_operation("TEST5")
    class Test5Operation(GenericOperation):
        """
        This operation will look for the environment variable TEST5_CONFIG_YAML,
        then inside that YAML file, it will find the key 'test5' and read steps_order, steps, etc.

        For example, if TEST5_CONFIG_YAML=/path/to/test5.yaml,
        it will load that file and expect something like:

            test5:
            record_final_state: true
            ...
            steps_order:
                ...
            steps:
                ...
        """

        def get_operation_name(self) -> str:
            # Tells the GenericOperation to look inside raw_config["test5"] in your YAML
            return "test5"
    