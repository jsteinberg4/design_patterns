package proxy_pattern;

public class Client {

  /**
   * Demo function for the database toy example of the ProxyPattern
   * @param args
   */
  public static void main(String[] args) {
    runWithoutProxy();
    runWithProxy();
  }

  /**
   * Demo with direct access to the Service classes
   */
  public static void runWithoutProxy() {

    System.out.println("Doing a database operation without a proxy: ----------");
    DatabaseService mongo = new MongoService();
    int query = 3245;
    int foundItem = mongo.findEntry(query);

    System.out.println(String.format("Direct from a database, query for %d found %d",
        query, foundItem));
    System.out.println("-------------------------------");
  }

  /**
   * Demo with a SimpleProxy
   */
  public static void runWithProxy() {
    System.out.println("Doing a database operation with a proxy: ----------");
    DatabaseService proxy = new SimpleProxy(new MongoService());
    int query = 3245;
    int foundItem = proxy.findEntry(query);

    System.out.println(String.format("Mongo lookup via proxy, query for %d found %d", query,
        foundItem));
    System.out.println("-------------------------------");
  }
}
