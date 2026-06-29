

# SchemaDefinition
<a name="API_SchemaDefinition"></a>

A schema definition for a gateway target. This structure defines the structure of the API that the target exposes.

## Contents
<a name="API_SchemaDefinition_Contents"></a>

 ** type **   <a name="bedrockagentcorecontrol-Type-SchemaDefinition-type"></a>
The type of the schema definition. This field specifies the data type of the schema.  
Type: String  
Valid Values: `string | number | object | array | boolean | integer`   
Required: Yes

 ** description **   <a name="bedrockagentcorecontrol-Type-SchemaDefinition-description"></a>
The description of the schema definition. This description provides information about the purpose and usage of the schema.  
Type: String  
Required: No

 ** items **   <a name="bedrockagentcorecontrol-Type-SchemaDefinition-items"></a>
The items in the schema definition. This field is used for array types to define the structure of the array elements.  
Type: [SchemaDefinition](#API_SchemaDefinition) object  
Required: No

 ** properties **   <a name="bedrockagentcorecontrol-Type-SchemaDefinition-properties"></a>
The properties of the schema definition. These properties define the fields in the schema.  
Type: String to [SchemaDefinition](#API_SchemaDefinition) object map  
Required: No

 ** required **   <a name="bedrockagentcorecontrol-Type-SchemaDefinition-required"></a>
The required fields in the schema definition. These fields must be provided when using the schema.  
Type: Array of strings  
Required: No

## See Also
<a name="API_SchemaDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/SchemaDefinition) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/SchemaDefinition) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/SchemaDefinition) 