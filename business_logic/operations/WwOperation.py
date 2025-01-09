from business_logic.generic_operation import GenericOperation
    from business_logic.operations_registry import register_operation

    @register_operation("WW")
    class WwOperation(GenericOperation):
        """
        This operation will look for the environment variable WW_CONFIG_YAML,
        then inside that YAML file, it will find the key 'ww' and read steps_order, steps, etc.

        For example, if WW_CONFIG_YAML=/path/to/ww.yaml,
        it will load that file and expect something like:

            ww:
            record_final_state: true
            ...
            steps_order:
                ...
            steps:
                ...
        """

        def get_operation_name(self) -> str:
            # Tells the GenericOperation to look inside raw_config["ww"] in your YAML
            return "ww"
    