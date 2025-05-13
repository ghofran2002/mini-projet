@Document(collection = "favorites")
public class Favorite {
    @Id
    private String id;
    private String userId;
    private String courseId;
    private String courseTitle;
}
