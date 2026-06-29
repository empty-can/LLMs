

# VpcConfig
<a name="API_VpcConfig"></a>

The configuration of a virtual private cloud (VPC). For more information, see [Protect your data using Amazon Virtual Private Cloud and AWS PrivateLink](https://docs.aws.amazon.com/bedrock/latest/userguide/usingVPC.html).

## Contents
<a name="API_VpcConfig_Contents"></a>

 ** securityGroupIds **   <a name="bedrock-Type-VpcConfig-securityGroupIds"></a>
An array of IDs for each security group in the VPC to use.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 5 items.  
Length Constraints: Minimum length of 0. Maximum length of 32.  
Pattern: `[-0-9a-zA-Z]+`   
Required: Yes

 ** subnetIds **   <a name="bedrock-Type-VpcConfig-subnetIds"></a>
An array of IDs for each subnet in the VPC to use.  
Type: Array of strings  
Array Members: Minimum number of 1 item. Maximum number of 16 items.  
Length Constraints: Minimum length of 0. Maximum length of 32.  
Pattern: `[-0-9a-zA-Z]+`   
Required: Yes

## See Also
<a name="API_VpcConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/VpcConfig) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/VpcConfig) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/VpcConfig) 