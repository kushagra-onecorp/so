def CreatePost_q(data):
    with connections['Freelancer'].cursor() as cursor:
        resp = cursor.execute(""" INSERT INTO dbfreelancersecond.JobAlert
                (
                SocialId,
                UserId,
                CompanyId,
                Title,
                ImageUrl,
                Description,
                IsInstaPost,
                IsFBPost,
                IsLinkedinPost,
                PostStatus,
                ScheduleDate,
                ToPost,
                IsDeleted,
                CreatedBy,
                UpdatedBy,
                CreatedAt,
                UpdatedAt)
                VALUES
                (UUID(),%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s); """, data)
        resp = cursor.lastrowid
        return resp


def SaveCredentials_q(data):
    with connections['Freelancer'].cursor() as cursor:
        resp = cursor.execute(""" INSERT INTO dbfreelancersecond.JobAlert
                (
                CredentialId,
                UserId,
                SocailUserName,
                SocialMediaAccessToken,
                SocialMediaName,
                IsDeleted,
                CreatedBy,
                UpdatedBy,
                CreatedAt,
                UpdatedAt)
                VALUES
                (UUID(),%s,%s,%s,%s,%s,%s,%s,%s,%s); """, data)
        resp = cursor.lastrowid
        return resp


def GetPosts_q(data):
    with connections['Freelancer'].cursor() as cursor:
        resp = cursor.execute(""" SELECT SocialId, UserId, CompanyId, Title, ImageUrl, Description, IsInstaPost, IsFBPost, IsLinkedinPost, PostStatus, ScheduleDate, ToPost, IsDeleted, CreatedBy, UpdatedBy, CreatedAt, UpdatedAt FROM dbfreelancersecond.JobAlert
        WHERE UserId IS
                (UUID(),%s,%s,%s,%s,%s,%s,%s,%s,%s); """, data)
        resp = cursor.lastrowid
        return resp
