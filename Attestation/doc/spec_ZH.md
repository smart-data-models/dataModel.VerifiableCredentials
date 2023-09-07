<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：证明  
=====<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.VerifiableCredentials/blob/master/Attestation/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全球描述：**EBSI可验证证明的模式**  
版本： 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 属性列表  

<sup><sub>[*] 如果属性中没有类型，是因为它可能有多个类型或不同的格式/模式</sub></sup>。  
- `credentialSchema[object]`: 包含有关可验证授权所依据的凭证模式（模板）的信息  	- `id[uri]`: 引用存储在（相关）可信模式注册表（TSR）上的凭证模式（模板），可验证授权正是基于该模式进行的    
- `credentialStatus[object]`: 包含有关如何验证可核实证明状态的信息（通过撤销和认可注册表，RER）。  	- `id[uri]`: 撤销和认可注册表 (RER) 中的参考记录，以便核查可核实证明的有效性    
	- `statusListCredential[uri]`: 引用 StatusList2021Credential 的 URL    
	- `statusListIndex[string]`: 以字符串形式表示的整数。基于零的索引值标识状态的位位置    
	- `statusPurpose[string]`: 状态条目的目的    
- `credentialSubject[object]`: 定义可验证证明所描述的主体信息  	  
- `evidence[array]`: 包含有关签发可核查证明的程序的信息  - `expirationDate[date-time]`: 定义可验证证明过期的日期和时间  - `id[uri]`: 定义可验证证明的唯一标识符  - `issuanceDate[date-time]`: 定义可验证证明生效的日期和时间  - `issued[date-time]`: 定义可验证证明的签发时间  - `issuer[uri]`: 定义可验证证明的签发人  - `proof[object]`: 包含有关证明的信息  	- `created[date-time]`: 定义创建校样的日期和时间    
	- `jws[string]`: 以 JWS 格式定义证明值    
	- `proofPurpose[string]`: 确定证明的目的    
	- `type[string]`: 定义证明类型    
- `type[array]`: 定义可验证凭据类型  - `validFrom[date-time]`: 定义可验证证明生效的日期和时间  - `validUntil[date-time]`: 定义可验证证明过期的日期和时间  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `credentialSchema`  - `credentialSubject`  - `id`  - `issuanceDate`  - `issued`  - `issuer`  - `type`  - `validFrom`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
源自 EBSI json 模式的数据模型 https://ec.europa.eu/digital-building-blocks/code/projects/EBSI/repos/json-schema/browse/schemas。@context 属性已从定义中删除，因为它在 NGSI-LD 中是强制性的，不需要明确记录。仅提供键值链接数据中的示例  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 属性的数据模型描述  
按字母顺序排列（点击查看详情）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
Attestation:    
  description: Schema of an EBSI Verifiable Attestation    
  properties:    
    credentialSchema:    
      description: Contains information about the credential schema (template) on which the Verifiable Authorisation is based    
      properties:    
        id:    
          description: References the credential schema (template) stored on the (relevant) Trusted Schemas Registry (TSR) on which the Verifiable Authorisation is based    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
        type:    
          description: Defines credential schema type    
          enum:    
            - FullJsonSchemaValidator2021    
          type: string    
          x-ngsi:    
            type: Property    
      required:    
        - id    
        - type    
      type: object    
      x-ngsi:    
        type: Property    
    credentialStatus:    
      description: 'Contains information about how to verify the status of the Verifiable Attestation (via the Revocation and Endorsement Registry, RER)'    
      properties:    
        id:    
          description: References record in the Revocation and Endorsement Registry (RER) to enable verification of a Verifiable Attestation’s validity    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
        statusListCredential:    
          description: URL referencing the StatusList2021Credential    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
        statusListIndex:    
          description: Integer expressed as a string. The zero based index value identifies the bit position of the status    
          type: string    
          x-ngsi:    
            type: Property    
        statusPurpose:    
          description: Purpose of the status entry    
          enum:    
            - revocation    
            - suspension    
          type: string    
          x-ngsi:    
            type: Property    
        type:    
          description: Defines the Verifiable Credential status type    
          type: string    
          x-ngsi:    
            type: Property    
      required:    
        - id    
        - type    
      type: object    
      x-ngsi:    
        type: Property    
    credentialSubject:    
      description: Defines information about the subject that is described by the Verifiable Attestation    
      properties:    
        id:    
          description: Defines the DID of the subject that is described by the Verifiable Attestation    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        type: Property    
    evidence:    
      description: Contains information about the process which resulted in the issuance of the Verifiable Attestation    
      items:    
        properties:    
          id:    
            description: 'If present, it MUST contain a URL that points to where more information about this instance of evidence can be found.'    
            type: string    
            x-ngsi:    
              type: Property    
          type:    
            description: Defines the evidence type    
            items:    
              type: string    
            type: array    
            x-ngsi:    
              type: Property    
        required:    
          - id    
          - type    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    expirationDate:    
      description: 'Defines the date and time, when the Verifiable Attestation expires'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      description: Defines unique identifier of the Verifiable Attestation    
      format: uri    
      type: string    
      x-ngsi:    
        type: Property    
    issuanceDate:    
      description: 'Defines the date and time, when the Verifiable Attestation becomes valid'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    issued:    
      description: Defines when the Verifiable Attestation was issued    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    issuer:    
      description: Defines the issuer of the Verifiable Attestation    
      format: uri    
      type: string    
      x-ngsi:    
        type: Property    
    proof:    
      description: Contains information about the proof    
      properties:    
        created:    
          description: 'Defines the date and time, when the proof has been created'    
          format: date-time    
          type: string    
          x-ngsi:    
            type: Property    
        jws:    
          description: Defines the proof value in JWS format    
          type: string    
          x-ngsi:    
            type: Property    
        proofPurpose:    
          description: Defines the purpose of the proof    
          type: string    
          x-ngsi:    
            type: Property    
        type:    
          description: Defines the proof type    
          type: string    
          x-ngsi:    
            type: Property    
        verificationMethod:    
          description: Contains information about the verification method / proof mechanisms    
          type: string    
          x-ngsi:    
            type: Property    
      required:    
        - type    
        - proofPurpose    
        - created    
        - verificationMethod    
        - jws    
      type: object    
      x-ngsi:    
        type: Property    
    type:    
      description: Defines the Verifiable Credential type    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    validFrom:    
      description: 'Defines the date and time, when the Verifiable Attestation becomes valid'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    validUntil:    
      description: 'Defines the date and time, when the Verifiable Attestation expires'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - issuer    
    - issuanceDate    
    - issued    
    - validFrom    
    - credentialSubject    
    - credentialSchema    
  type: object    
  x-derived-from: https://ec.europa.eu/digital-building-blocks/code/projects/EBSI/repos/json-schema/browse/schemas/ebsi-attestation/2022-11/schema.json    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.VerifiableCredentials/blob/master/Attestation/LICENSE.md    
  x-model-schema: ""    
  x-model-tags: 'EBSI, Verifiable Credentials'    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## 有效载荷示例  
以 JSON-LD 格式作为键值的 Attestation 示例不可用。当使用 `options=keyValues` 时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
未提供规范化 JSON-LD 格式的 "证明 "示例。在不使用选项时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
#### 认证 NGSI-LD 密钥值示例  
下面是一个以 JSON-LD 格式作为键值的 "证明 "示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "@context": ["https://www.w3.org/2018/credentials/v1"],  
  "id": "urn:uuid:003a1dd8-a5d2-42ef-8182-e921c0a9f2cd",  
  "type": ["VerifiableCredential", "VerifiableAttestation"],  
  "issuer": "did:ebsi:00001234",  
  "issuanceDate": "2021-11-01T00:00:00Z",  
  "validFrom": "2021-11-01T00:00:00Z",  
  "expirationDate": "2024-06-22T14:11:44Z",  
  "issued": "2020-06-22T14:11:44Z",  
  "credentialSubject": {  
    "id": "did:ebsi:00001235"  
  },  
  "credentialStatus": {  
    "id": "https://api-test.ebsi.eu/trusted-issuers-registry/v3/issuers/did:ebsi:zyrMG8T9xYbNoSwyQa4SGMJ/proxy/6cc5fcc621d8098977d378ec7bf63f9ad0b204d56bb604f75bc9290e7033ac84/credentials/status/5#129430",  
    "type": "StatusList2021Entry",  
    "statusPurpose": "revocation",  
    "statusListIndex": "129430",  
    "statusListCredential": "https://api-test.ebsi.eu/trusted-issuers-registry/v3/issuers/did:ebsi:zyrMG8T9xYbNoSwyQa4SGMJ/proxy/6cc5fcc621d8098977d378ec7bf63f9ad0b204d56bb604f75bc9290e7033ac84/credentials/status/5"  
  },  
  "credentialSchema": {  
    "id": "https://api-test.ebsi.eu/trusted-schemas-registry/v2/schemas/0xf30fd418c8b2c1534b0685e12b044d3d29284fe37762a45d0c1e5601eed3d1d9",  
    "type": "FullJsonSchemaValidator2021"  
  }  
}  
```  
</details>  
未提供规范化 JSON-LD 格式的 "证明 "示例。当不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
<!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
请参阅 [FAQ 10](https://smartdatamodels.org/index.php/faqs/)，获取如何处理幅度单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
