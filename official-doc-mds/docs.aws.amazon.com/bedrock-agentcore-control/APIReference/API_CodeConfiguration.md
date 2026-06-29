

# CodeConfiguration
<a name="API_CodeConfiguration"></a>

The configuration for the source code that defines how the agent runtime code should be executed, including the code location, runtime environment, and entry point.

## Contents
<a name="API_CodeConfiguration_Contents"></a>

 ** code **   <a name="bedrockagentcorecontrol-Type-CodeConfiguration-code"></a>
The source code location and configuration details.  
Type: [Code](API_Code.md) object  
 **Note: **This object is a Union. Only one member of this object can be specified or returned.  
Required: Yes

 ** entryPoint **   <a name="bedrockagentcorecontrol-Type-CodeConfiguration-entryPoint"></a>
The entry point for the code execution, specifying the function or method that should be invoked when the code runs.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 2 items.  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Required: Yes

 ** runtime **   <a name="bedrockagentcorecontrol-Type-CodeConfiguration-runtime"></a>
The runtime environment for executing the agent code. Specify the programming language and version to use for the agent runtime. For valid values, see the list of supported runtimes.  
Type: String  
Valid Values: `PYTHON_3_10 | PYTHON_3_11 | PYTHON_3_12 | PYTHON_3_13 | PYTHON_3_14 | NODE_22`   
Required: Yes

## See Also
<a name="API_CodeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/CodeConfiguration) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/CodeConfiguration) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/CodeConfiguration) 