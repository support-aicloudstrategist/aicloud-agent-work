# LinkedIn Post — S3 Storage Tier Mismatch (Post B: Practical FinOps Tip)

---

Most teams have cold data aging quietly in S3 Standard. You're paying Standard prices for objects nobody has touched in six months.

In ap-south-1, S3 Standard costs $0.025/GB/month. Glacier Instant Retrieval costs $0.005/GB/month — the same millisecond-latency retrieval, one-fifth the price. On 1 TB of cold objects, that's $20.48/month saved, or ~$246/year, for a one-time lifecycle rule.

**10-minute check you can run now:**

```bash
# List Standard-class objects last modified before 90 days ago
aws s3api list-objects-v2 \
  --bucket YOUR_BUCKET \
  --query "Contents[?StorageClass=='STANDARD'].[Key,Size,LastModified]" \
  --output text | awk '$3 < "2026-01-15"' | sort -k2 -rn | head -20
```

If that returns hundreds of rows, you have a lifecycle gap.

Fix: add an S3 Lifecycle rule — transition objects with zero GET activity after 30 days to Glacier Instant Retrieval. AWS S3 Storage Lens shows per-bucket access patterns if you want data before committing.

Cold data in Standard is a tax on inattention.

---
*AICloudStrategist | FinOps for AWS teams*
