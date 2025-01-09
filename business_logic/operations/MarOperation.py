from business_logic.generic_operation import GenericOperation
    from business_logic.operations_registry import register_operation

    @register_operation("MAR")
    class MarOperation(GenericOperation):
        """
        This operation will look for the environment variable MAR_CONFIG_YAML,
        then inside that YAML file, it will find the key 'mar' and read steps_order, steps, etc.

        For example, if MAR_CONFIG_YAML=/path/to/mar.yaml,
        it will load that file and expect something like:

            mar:
            record_final_state: true
            ...
            steps_order:
                ...
            steps:
                ...
        """

        def get_operation_name(self) -> str:
            # Tells the GenericOperation to look inside raw_config["mar"] in your YAML
            return "mar"
    