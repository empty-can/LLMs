

# RatingScale
<a name="API_RatingScale"></a>

 The rating scale that defines how evaluators should score agent performance, supporting both numerical and categorical scales. 

## Contents
<a name="API_RatingScale_Contents"></a>

**Important**  
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** categorical **   <a name="bedrockagentcorecontrol-Type-RatingScale-categorical"></a>
 The categorical rating scale with named categories and definitions for qualitative evaluation.   
Type: Array of [CategoricalScaleDefinition](API_CategoricalScaleDefinition.md) objects  
Required: No

 ** numerical **   <a name="bedrockagentcorecontrol-Type-RatingScale-numerical"></a>
 The numerical rating scale with defined score values and descriptions for quantitative evaluation.   
Type: Array of [NumericalScaleDefinition](API_NumericalScaleDefinition.md) objects  
Required: No

## See Also
<a name="API_RatingScale_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-agentcore-control-2023-06-05/RatingScale) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-agentcore-control-2023-06-05/RatingScale) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-agentcore-control-2023-06-05/RatingScale) 