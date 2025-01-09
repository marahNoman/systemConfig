from business_logic.generic_operation import GenericOperation
    from business_logic.operations_registry import register_operation

    @register_operation("SS")
    class SsOperation(GenericOperation):
        """
        This operation will look for the environment variable SS_CONFIG_YAML,
        then inside that YAML file, it will find the key 'ss' and read steps_order, steps, etc.

        For example, if SS_CONFIG_YAML=/path/to/ss.yaml,
        it will load that file and expect something like:

            ss:
            record_final_state: true
            ...
            steps_order:
                ...
            steps:
                ...
        """

        def get_operation_name(self) -> str:
            # Tells the GenericOperation to look inside raw_config["ss"] in your YAML
            return "ss"
    