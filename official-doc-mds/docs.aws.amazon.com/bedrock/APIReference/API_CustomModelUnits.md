

# CustomModelUnits
<a name="API_CustomModelUnits"></a>

A `CustomModelUnit` (CMU) is an abstract view of the hardware utilization that Amazon Bedrock needs to host a single copy of your custom model. A model copy represents a single instance of your imported model that is ready to serve inference requests. Amazon Bedrock determines the number of custom model units that a model copy needs when you import the custom model. 

You can use `CustomModelUnits` to estimate the cost of running your custom model. For more information, see [Calculate the cost of running a custom model](https://docs.aws.amazon.com/bedrock/latest/userguide/import-model-calculate-cost.html).

## Contents
<a name="API_CustomModelUnits_Contents"></a>

 ** customModelUnitsPerModelCopy **   <a name="bedrock-Type-CustomModelUnits-customModelUnitsPerModelCopy"></a>
The number of custom model units used to host a model copy.   
Type: Integer  
Required: No

 ** customModelUnitsVersion **   <a name="bedrock-Type-CustomModelUnits-customModelUnitsVersion"></a>
The version of the custom model unit. Use to determine the billing rate for the custom model unit.  
Type: String  
Pattern: `v\d+.\d+`   
Required: No

## See Also
<a name="API_CustomModelUnits_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/CustomModelUnits) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/CustomModelUnits) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/CustomModelUnits) 