provider "aws" {  
    region = "us-west-2"
}
resource "aws_s3_bucket" "vulnerable_bucket" {  
    bucket = "rb-test-131233"  
    acl    = "public-read" 
    
    versioning {    
        enabled = false  
    }  
    
    server_side_encryption_configuration {    
        rule {      
            apply_server_side_encryption_by_default {        
                sse_algorithm = "AES256"      
            }      
            bucket_key_enabled = false    
        }  
    }
}
